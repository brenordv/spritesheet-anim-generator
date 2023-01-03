# -*- coding: utf-8 -*-

# The frames here are already adjusted according to the Guide.
base_anim_config = [
    {
        "name": "Walk_",
        "indexes": [0, 1, 2, 1, 0, 1],
    },
    {
        "name": "Lift_",
        "indexes": [3, 4, 5, 4, 3, 4],
    },
    {
        "name": "Crouch_",
        "indexes": [6, ],
    },
    {
        "name": "Jump_",
        "indexes": [6, 7, 8, 9],
    },
    {
        "name": "Attack_",
        "indexes": [10, 11, 12, 13, 14],
    },
    {
        "name": "NockBow_",
        "indexes": [15, ],
    },
    {
        "name": "Bow_",
        "indexes": [16, 17, 18, 17, 16, 17],
    },
    {
        "name": "Climb_",
        "indexes": [19, 20, 21, 20, 19, 20],
    },
    {
        "name": "Sleep_",
        "indexes": [22, ],
    }
]


def create_anim_configs():
    """
    Adapt the base configuration so we can fetch all the correct frames for all the animations.
    """
    to_create = [
        {
            "direction": "S",
            "offset": 0
        },
        {
            "direction": "W",
            "offset": 23
        },
        {
            "direction": "E",
            "offset": 46
        },
        {
            "direction": "N",
            "offset": 69
        }
    ]

    directions = []
    for item in to_create:
        direction, offset = item.values()
        for base_config in base_anim_config:
            direction_name = f"{base_config['name']}{direction}"
            if direction == "S":
                indexes = base_config['indexes']
            else:
                indexes = [i + offset if i > 0 else i + offset+1 for i in base_config['indexes']]
            directions.append({
                "direction": direction_name,
                "indexes": indexes
            })

    return directions