import os

from django.conf import settings
from django.core.management.base import BaseCommand

from core.djangoapps.resources.models import (AttributeType, Resource,
                                              ResourceAttribute,
                                              ResourceAttributeType,
                                              ResourceType)

base_dir = settings.BASE_DIR

class Command(BaseCommand):

    def handle(self, *args, **options):

        with open(os.path.join(base_dir, 'local_data/R1_attribute_types.tsv')) as file:
            for name in file:
                attribute_type_obj, created = AttributeType.objects.get_or_create(
                    name=name.strip())
                print(attribute_type_obj, created)

        with open(os.path.join(base_dir, 'local_data/R2_resource_types.tsv')) as file:
            for line in file:
                name, description = line.strip().split('\t')
                resource_type_obj, created = ResourceType.objects.get_or_create(
                    name=name.strip(), description=description.strip())
                print(resource_type_obj, created)

        with open(os.path.join(base_dir, 'local_data/R3_resource_attributes_types.tsv')) as file:
            for line in file:
                attribute_type_name, resource_type_name, name, required = line.strip().split('\t')
                resource_attribute_type_obj, created = ResourceAttributeType.objects.get_or_create(
                    attribute_type=AttributeType.objects.get(
                        name=attribute_type_name),
                    name=name,
                    required=bool(required))
                print(resource_attribute_type_obj, created)

        with open(os.path.join(base_dir, 'local_data/R4_resources.tsv')) as file:
            for line in file:
                resource_type_name, name, description = line.strip().split('\t')
                resource_attribute_type_obj, created = Resource.objects.get_or_create(
                    resource_type=ResourceType.objects.get(name=resource_type_name),
                    name=name,
                    description=description.strip())
                print(resource_attribute_type_obj, created)
        with open(os.path.join(base_dir, 'local_data/R5_resource_attributes.tsv')) as file:
            for line in file:
                resource_type_name, resource_attribute_type_name, resource_attribute_type_type_name, resource_name, value = line.strip().split('\t')
                resource_attribute_obj, created = ResourceAttribute.objects.get_or_create(
                    resource_attribute_type=ResourceAttributeType.objects.get(name=resource_attribute_type_name, attribute_type__name=resource_attribute_type_type_name),
                    resource=Resource.objects.get(name=resource_name),
                    value=value.strip())
                print(resource_attribute_obj, created)