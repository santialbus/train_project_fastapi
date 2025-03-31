import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"
    moderator = "moderator"
