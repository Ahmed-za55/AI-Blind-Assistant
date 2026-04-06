import time

_last_navigation_time = 0
NAVIGATION_COOLDOWN = 3

def navigate(objects, frame_width):
    global _last_navigation_time

    if not objects:
        return None

    now = time.time()
    if now - _last_navigation_time < NAVIGATION_COOLDOWN:
        return None

    for name, area, x1, x2 in objects:
        center = (x1 + x2) // 2

        if area > 60000:
            _last_navigation_time = now
            return f"Stop! {name} very close"
        elif center < frame_width // 3:
            _last_navigation_time = now
            return f"{name} on your left"
        elif center > frame_width * 2 // 3:
            _last_navigation_time = now
            return f"{name} on your right"
        else:
            _last_navigation_time = now
            return f"{name} ahead"

    return None