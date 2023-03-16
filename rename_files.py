from datetime import datetime

# ORGANIZE
# group by city
# date order within city group
# assign consecutive numbers to photos

# RENAME
# adding leading zeros so all numers same length within group  i.e. if len(num) > 1 <= 10 add 0, accont up to 100
# name = city01.ext


class Photo:
    def __init__(self, string):
        split_str = string.split(", ")
        self.name = split_str[0].split(".")[0]
        self.ext = f".{split_str[0].split('.')[1]}"
        self.city = split_str[1]
        self.date_time = datetime.strptime(split_str[2], "%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.name


def get_photo_objs(list):
    """Return list of Photo objects from list filename strings."""
    photos = [Photo(filename) for filename in list]

    return photos


def get_cities_set(photo_list):
    """
    Return unique set of cities from list of photo objects.
    e.g. [{'Paris': []}, {'Warsaw': []}, {'London': []}]
    """
    cities = [i.city for i in photo_list]
    cities_set = set(cities)

    return cities_set


def group_photos_by_city(photo_objs, dictionary):
    """
    Add photo objects to the correct dict. 
    """
    for photo in photo_objs:
        for dictionary in city_dicts:
            if photo.city in dictionary.keys():
                dictionary[photo.city].append(photo)
                break

    return dictionary


def sort_by_date(city_dicts):
    """Sort city_dicts in date order, edit in place."""
    for dict in city_dicts:
        for key, value in dict.items():
            value = sorted(value, key=lambda x: x.date_time)
            dict[key] = value


def get_city_list_dicts(cities_set):
    """Create 2 x lists of dicts; to hold photo class objects and pretty_names organised in city groups."""
    city_dicts = []
    pretty_names_dict = []

    for i in cities_set:
        city_dicts.append({i: []})
        pretty_names_dict.append({i: []})

    return city_dicts, pretty_names_dict


if __name__ == "__main__":
    strings = ["g.jpg, Warsaw, 2016-02-29 22:13:11",
               "me.jpg, Warsaw, 2013-09-06 15:40:22",
               "myFriends.png, Warsaw, 2013-09-05 14:07:13",
               "notredame.png, Paris, 2015-09-01 12:00:00",
               "photo.jpg, Warsaw, 2013-09-05 14:08:15",
               "pisatower.jpg, Paris, 2015-07-22 23:59:59",
               "BOB.jpg, London, 2015-08-05 00:02:03",
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02",
               "Jay.png, London, 2015-06-20 15:13:22",
               "a.png, Warsaw, 2016-02-13 13:33:50",
               "b.jpg, Warsaw, 2016-01-02 15:12:22",
               "c.jpg, Warsaw, 2016-01-02 14:34:30",
               "d.jpg, Warsaw, 2016-01-02 15:15:01",
               "e.png, Warsaw, 2016-01-02 09:49:09",
               "f.png, Warsaw, 2016-01-02 10:55:32"]

    photo_objs = get_photo_objs(strings)
    cities_set = get_cities_set(photo_objs)
    city_dicts, pretty_names_dict = get_city_list_dicts(cities_set)

    group_photos_by_city(photo_objs, city_dicts)
    sort_by_date(city_dicts)

    for i in city_dicts:
        for key, value in i.items():
            list_length = len(value)
            for index, photo in enumerate(value):
                if list_length >= 100:
                    one_zero_pattern = '{:>03}'
                elif list_length >= 10:
                    one_zero_pattern = '{:>02}'
                else:
                    one_zero_pattern = '{:>01}'

                digits = one_zero_pattern.format(index+1)
                pretty_name = photo.city + digits + photo.ext
                print(pretty_name)

                for dictionary in pretty_names_dict:
                    for key, value in dictionary.items():
                        if photo.city in key:
                            value.append(pretty_name)

    print(pretty_names_dict)
