from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Cart, CartItem, OrderItem, Order

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'address', 'phone_number')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        product_instance = validated_data.pop('product')
        # Use product_instance attributes directly for get_or_create
        product_instance, created = Product.objects.get_or_create(
            id=product_instance.id,
            defaults={
                'name': product_instance.name,  # Example: Replace with actual fields
                'description': product_instance.description  # Example: Replace with actual fields
                # Add other fields as needed
            }
        )
        cart_item = CartItem.objects.create(product=product_instance, **validated_data)
        return cart_item

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'items', 'created_at', 'updated_at', 'user')

    def create(self, validated_data):
        # TODO: cart created but with empty items.
        #  FIXED THIS by creating cart bydefault when user is created/onboarded.
        items_data = validated_data.pop('items', None)
        cart = Cart.objects.create(**validated_data)
        if items_data:
            for item_data in items_data:
                product_instance = item_data.pop('product')
                product_instance, created = Product.objects.get_or_create(
                    id=product_instance.id,
                    defaults={
                        'name': product_instance.name,  # Example: Replace with actual fields
                        'description': product_instance.description  # Example: Replace with actual fields
                    }
                )
                CartItem.objects.create(cart=cart, product=product_instance, **item_data)
        return cart

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        if items_data:
            # Get existing items related to the instance
            existing_items = instance.items.all()
            existing_item_ids = [item.id for item in existing_items]

            # Update existing items or create new items if they don't exist
            for item_data in items_data:
                product_data = item_data.pop('product')
                product_id = product_data.id
                quantity = item_data.get('quantity')

                # Check if the item already exists in the cart
                if product_id in existing_item_ids:
                    cart_item = CartItem.objects.get(cart=instance, product_id=product_id)
                    cart_item.quantity = quantity
                    cart_item.save()
                else:
                    # Create new cart item if it doesn't exist
                    product_instance = Product.objects.get(pk=product_id)
                    instance.items.create(product=product_instance, quantity=quantity)

            # Delete items that are no longer in the updated items_data
            for existing_item in existing_items:
                if existing_item.id not in [item_data.get('id') for item_data in items_data]:
                    existing_item.delete()

        return instance
    # def update(self, instance, validated_data):
    #     items_data = validated_data.pop('items', None)
    #     if items_data:
    #         instance.items.clear()  # Clear existing items before adding updated ones
    #         for item_data in items_data:
    #             product_data = item_data.pop('product')
    #             product_id = product_data.id
    #             quantity = item_data.get('quantity')
    #             product_instance = Product.objects.get(pk=product_id)
    #             instance.items.create(product=product_instance, quantity=quantity)
    #     return instance


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
