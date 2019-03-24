from geopy.geocoders import Nominatim
from geopy.geocoders.base import DEFAULT_SENTINEL

__all__ = ("PickPoint",)


class PickPoint(Nominatim):
    """PickPoint geocoder is a commercial version of Nominatim.

    Documentation at:
       https://pickpoint.io/api-reference
    """

    geocode_path = '/v1/forward'
    reverse_path = '/v1/reverse'

    def __init__(
            self,
            api_key,
            *,
            format_string=None,
            timeout=DEFAULT_SENTINEL,
            proxies=DEFAULT_SENTINEL,
            domain='api.pickpoint.io',
            scheme=None,
            user_agent=None,
            ssl_context=DEFAULT_SENTINEL
    ):
        """

        :param str api_key: PickPoint API key obtained at
            https://pickpoint.io.

        :param str format_string:
            See :attr:`geopy.geocoders.options.default_format_string`.

        :param int timeout:
            See :attr:`geopy.geocoders.options.default_timeout`.

        :param dict proxies:
            See :attr:`geopy.geocoders.options.default_proxies`.

        :param str domain: Domain where the target Nominatim service
            is hosted.

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`.

        :param str user_agent:
            See :attr:`geopy.geocoders.options.default_user_agent`.

        :type ssl_context: :class:`ssl.SSLContext`
        :param ssl_context:
            See :attr:`geopy.geocoders.options.default_ssl_context`.
        """

        super().__init__(
            format_string=format_string,
            timeout=timeout,
            proxies=proxies,
            domain=domain,
            scheme=scheme,
            user_agent=user_agent,
            ssl_context=ssl_context,
        )
        self.api_key = api_key

    def _construct_url(self, base_api, params):
        """
        Construct geocoding request url. Overridden.

        :param str base_api: Geocoding function base address - self.api
            or self.reverse_api.

        :param dict params: Geocoding params.

        :return: string URL.
        """
        params['key'] = self.api_key
        return super()._construct_url(base_api, params)
