from rest_framework.throttling import UserRateThrottle
class ChRateThrottle(UserRateThrottle):
    scope = 'ch'