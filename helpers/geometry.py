from shapely.geometry import Point, Polygon

# Function to check if a point is inside a polygon
def is_point_in_polygon(point, polygon):
    return polygon.contains(Point(point))

# Function to filter places based on the polygon
def filter_places_by_polygon(places, polygon_coords):
    polygon = Polygon(polygon_coords)
    return [place for place in places if is_point_in_polygon((place['geometry']['location']['lat'], place['geometry']['location']['lng']), polygon)]
