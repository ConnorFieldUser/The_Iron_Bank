
from rest_framework import serializers

from bank_records_app.models import Transaction


# class TransactionSerializer(serializers.ModelSerializer):
#     user = serializers.HyperlinkedRelatedField(
#         many=True,
#         view_name="ingredient_detail_update_destroy_api_view",
#         read_only=True,
#     )
#     # created_by = serializers.ReadOnlyField()
#     calorie_count = serializers.ReadOnlyField()
#     my_favorite = serializers.SerializerMethodField()
#     user = serializers.ReadOnlyField(source="created_by.id")
#
#     def get_my_favorite(self, obj):
#         return "PANCAKES!!!!"
#
#     class Meta:
#         model = Transaction
#         exclude = ('created_by',)


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
