from enum import Enum

from .base import Ward, District, Province, VietNamDivisionType


class ProvinceEnum(Province, Enum):
    HA_NOI = Province('Thành phố Hà Nội', 1, VietNamDivisionType.THANH_PHO_TRUNG_UONG, 'thanh_pho_ha_noi', 24)


class DistrictEnum(District, Enum):
    LAK_DL = District("Huyện Lắk", 656, VietNamDivisionType.HUYEN, "huyen_lak", 66)


class WardEnum(Ward, Enum):
    UY_NO_DA = Ward("Xã Uy Nỗ", 478, VietNamDivisionType.XA, "xa_uy_no", 17)