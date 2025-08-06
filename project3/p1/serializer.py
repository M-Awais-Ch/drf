from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['roll','name','dep']
        # or we can use this--->> fields='__all__'

    #Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # object  level validation when multiple fields validate

    def validate(self, data):
        rol = data.get('roll')
        nam = data.get('name')
        if rol >= 400 and nam.upper() == 'CHANGE':
            raise serializers.ValidationError('Wrong Information')
        return data

    #Vlaidators

    def starts_with_a(value):
        if value[0] == 'a':
            raise serializers.ValidationError('Name must start with the letter "A".')
        return value

    name = serializers.CharField(validators=[starts_with_a])













    # def create(self,validated_data):
    #     return Student.objects.create(**validated_data)
    #
    # def update(self,instance,validated_data):
    #     print(instance.name)
    #     instance.name=validated_data.get('name',instance.name)
    #     print(instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.dep = validated_data.get('dep', instance.dep)
    #     instance.save()
    #     return instance

    # def validate_roll(self,value):
    #     if value>=200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value
    # object level validation when multiple fileds validate
    # def validate(self,data):
    #     rol=data.get('roll')
    #     nam=data.get('name')
    #     if rol>=400 and nam.upper()=='GMD':
    #         raise serializers.ValidationError('Wrong Information')
    #     return data
