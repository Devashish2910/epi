"""
Rectangle Intersection
"""
# Case 1: Find x, y, height, width
r1 = {"x": 2, "y": 1, "height": 3, "width": 3}
r2 = {"x": 3, "y": 3, "height": 2, "width": 1}

def rectangle_intersection(r1, r2):
    if is_intersect(r1, r2):
        lb_x = max(r1["x"], r2["x"])
        lb_y = max(r1["y"], r2["y"])
        width = min(r1["x"]+r1["width"], r2["x"]+r2["width"]) - max(r1["x"], r2["x"])
        height = min(r1["y"]+r1["height"], r2["y"]+r2["height"]) - max(r1["y"], r2["y"])

        return {"x": lb_x, "y": lb_y, "height": height, "width": width}
    else:
        return None

def is_intersect(r1, r2):
    return True if r1["x"] + r1["width"] >= r2["x"] and r2["x"] + r2["width"] >= r1["x"] and r1["y"] + r1["height"] >= r2["y"] and r2["y"] + r1["height"] >= r1["y"] else False

print(rectangle_intersection(r1, r2))


# Case 2: Find area of overlapping rectangle
r1 = {"x1": 2, "y1": 1, "x2": 5, "y2": 4}
r2 = {"x1": 3, "y1": 3, "x2": 5, "y2": 5}

def area_of_intersection(r1, r2):
    width = min(r1["x2"], r2["x2"]) - max(r1["x1"], r2["x1"])
    height = min(r1["y2"], r2["y2"]) - max(r1["y1"], r2["y1"])

    return width * height if width > 0 else None

print(area_of_intersection(r1, r2))

