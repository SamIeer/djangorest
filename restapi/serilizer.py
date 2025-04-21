from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Student 
        fields = '__all__'
        # fields = ['name' , 'age']
        # exclude = ['id']


# adding coustom validations in serliazer
    def validate(self , data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error':"age cannot be less than 18"})
    
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({'Error':"name cant have number"})
        return data