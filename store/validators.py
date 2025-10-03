from django.core.exceptions import ValidationError


# Validator function for images
def validate_file_size(file):
    max_size_in_kb = 1000
    
    if file.size > (max_size_in_kb * 1024):
        raise ValidationError(f"File size can not be larger than {max_size_in_kb} KB")
    