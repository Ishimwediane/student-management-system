from models.enums import Level, FieldOfStudy


class Validator:
    """
    Validation utility class for student management system
    """
    
    @staticmethod
    def parse_level(level_str: str) -> Level:
       
        try:
            return Level(level_str.lower().strip())
        except ValueError:
            raise ValueError(f"Invalid level '{level_str}'. Must be one of: {[lvl.value for lvl in Level]}")
    
    @staticmethod
    def parse_field_of_study(field_str: str) -> FieldOfStudy:
        
        try:
            return FieldOfStudy(field_str.lower().strip())
        except ValueError:
            raise ValueError(f"Invalid field of study '{field_str}'. Must be one of: {[f.value for f in FieldOfStudy]}")
    
    @staticmethod
    def parse_multiple_levels(level_input: str) -> list[Level]:
        
        if level_input.strip().lower() == "all":
            return list(Level)
        
        levels = []
        for level_str in level_input.split(","):
            level_str = level_str.strip()
            if level_str:
                levels.append(Validator.parse_level(level_str))
        return levels
    
    @staticmethod
    def parse_multiple_fields(field_input: str) -> list[FieldOfStudy]:
        
        if field_input.strip().lower() == "all":
            return list(FieldOfStudy)
        
        fields = []
        for field_str in field_input.split(","):
            field_str = field_str.strip()
            if field_str:
                fields.append(Validator.parse_field_of_study(field_str))
        return fields