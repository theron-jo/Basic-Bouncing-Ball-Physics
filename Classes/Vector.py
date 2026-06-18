import math

def get_mag(coord: list[int]):
        mag = math.sqrt((coord[0]**2) + (coord[1]**2))
        return mag

        
def normalize(coord: list[int]):
        mag = get_mag(coord)
        if mag == 0:
            return [0,0]
        else:
            return [coord[0]/mag, coord[1]/mag]

def rotate(coord, angle):
        mag = get_mag(coord)
        if mag == 0:
            return
        else:
            coord_normal = normalize(coord)
            cur_angle = math.degrees(math.cos(coord_normal[0]))
            new_angle = cur_angle + angle
            rotated_norm = [(math.cos(math.radians(new_angle))), (math.sin(math.radians(new_angle)))]
            rotated_coord = [(rotated_norm[0]*mag), (rotated_norm[1]*mag)]
            return rotated_coord

def get_relative_vector(vect1, vect2):
        dx = vect2[0] - vect1[0]
        dy = vect2[1] - vect1[1]
        relative_vect = [dx, dy]
        return relative_vect

def get_distance(vect1, vect2):
        dx = (vect2[0] - vect1[0])
        dy = (vect2[1] - vect1[1])
        distance = math.sqrt((dx**2) + (dy**2))
        return distance

def get_reflect_angle(vect1, vect2):
        inc_angle_rad = math.atan2(vect2.pos[0] - vect1.pos[0], vect2.pos[1] - vect1.pos[1])
        inc_angle_degree = math.degrees(inc_angle_rad)
        reflect_angle = (2 * inc_angle_rad) - inc_angle_degree
        return reflect_angle

def get_dot(vect1, vect2):
      dot = (vect1[0]*vect2[0]) + (vect1[1]*vect2[1])
      return dot
        
