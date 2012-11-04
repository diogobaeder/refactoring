class OfferFinder(object):
    def find_for(self, user):
        offers = []

        if not user['likes_sports'] and user['belly_size'] == 'big':
            offers.append('Videogame console')

        if user['likes_sports'] and user['tshirt_size'] == 'medium':
            offers.append('Football t-shirt')

        return offers