# ARCHHELP — G‘isht kalkulyatori

def calculate_bricks(
    wall_length,
    wall_height,
    brick_length,
    brick_width,
    brick_height,
    wall_thickness,
    mortar=0.01,
    waste_percent=5
):
    """
    G‘isht devori uchun taxminiy material hisob-kitobi.
    Barcha o‘lchamlar metrda.
    """

    # G‘ishtning mortar bilan birga modul o‘lchamlari
    module_length = brick_length + mortar
    module_height = brick_height + mortar

    # Devorning umumiy yuzasi
    wall_area = wall_length * wall_height

    # Tanlangan devor qalinligi
    thickness_map = {
        0.5: brick_width,
        1.0: brick_length,
        1.5: brick_length + brick_width,
        2.0: brick_length * 2
    }

    if wall_thickness not in thickness_map:
        raise ValueError("Devor qalinligi noto‘g‘ri tanlangan.")

    wall_thickness_m = thickness_map[wall_thickness]

    # Devor hajmi
    wall_volume = wall_area * wall_thickness_m

    # Bitta g‘ishtning hajmi
    brick_volume = brick_length * brick_width * brick_height

    # Taxminiy sof g‘isht soni
    brick_count = wall_volume / brick_volume

    # Zaxira
    reserve = brick_count * (waste_percent / 100)

    # Buyurtma uchun yaxlitlangan son
    total_bricks = int(brick_count + reserve + 0.9999)

    return {
        "wall_area": wall_area,
        "wall_volume": wall_volume,
        "brick_count": int(brick_count + 0.5),
        "reserve": int(reserve + 0.5),
        "total_bricks": total_bricks
    }