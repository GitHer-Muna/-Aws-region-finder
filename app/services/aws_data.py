AWS_REGION_DATA = {
    "India": [{"code": "ap-south-1", "name": "Asia Pacific (Mumbai)"}],
    "United States": [
        {"code": "us-east-1", "name": "US East (N. Virginia)"},
        {"code": "us-west-2", "name": "US West (Oregon)"}
    ],
    "Germany": [{"code": "eu-central-1", "name": "EU (Frankfurt)"}]
}

async def get_aws_regions_by_country(country: str):
    return AWS_REGION_DATA.get(country.title(), [])
