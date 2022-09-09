class Receipt:
    attributes = ['taxpayer_number', 'taxpayer_name', 'taxpayer_address', 'taxpayer_city', 'taxpayer_state', 'taxpayer_zip', 'taxpayer_county', 'location_number', 'location_name', 'location_address', 'location_city', 'location_state', 'location_zip', 'location_county', 'inside_outside_city_limits_code_y_n', 'tabc_permit_number', 'responsibility_begin_date_yyyymmdd', 'responsibility_end_date_yyyymmdd', 'obligation_end_date_yyyymmdd', 'liquor_receipts', 'wine_receipts', 'beer_receipts', 'cover_charge_receipts', 'total_receipts']

    def __init__(self, **kwargs):
        # validate the keyword arguments are in attrubutes
        for key in kwargs.keys():
            if key not in self.attributes:
                raise ValueError(f"{key} not in {self.attributes}")

        # set class attributes from the keyword arguments
        for k, v in kwargs.items():
            setattr(self, k, v)

