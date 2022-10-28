from rest_framework import serializers
from applic.models import Details,Bill

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields=(
            'billno',
            'bname',
            'baddress',
            'bphonenumber',
            'sname',
            'saddress',
            'sphonenumber'

        )
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields=(
            'billno',
            'slno',
            'product',
            'quantity',
            'price',
            'total',

        )


