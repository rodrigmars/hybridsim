from os.path import dirname, join

def configuration() -> dict:

    root_dir = dirname(__file__)

    root_images = join(root_dir, 'images', 'tanks')

    back_stage = join(root_dir, 'images', 'tanks', 'stage.png')

    tank_a = join(root_dir, 'images', 'tanks', 't_01')

    tank_b = join(root_dir, 'images', 'tanks', 't_02')

    tank_c = join(root_dir, 'images', 'tanks', 't_03')

    return {"root_images": root_images, "back_stage": back_stage,
            "tank_a": tank_a, "tank_b": tank_b, "tank_c": tank_c}
