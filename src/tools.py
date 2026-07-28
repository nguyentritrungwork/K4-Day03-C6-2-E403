"""
🛠️ TOOL REGISTRY & SCHEMAS (Dành cho Role 2: Tool & Spec Engineer)
Nơi khai báo tất cả các "món đồ nghề" mà ReAct Agent có thể gọi.

Đề tài: Trợ Lý Tìm & Đặt Lịch Xem Nhà Trọ / Căn Hộ Cho Thuê
"""

from typing import Optional


# =============================================================================
# 1. search_properties — Tìm kiếm nhà trọ / căn hộ cho thuê
# =============================================================================
def search_properties(
    location: str,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    property_type: Optional[str] = None,
    bedrooms: Optional[int] = None,
) -> str:
    """
    Tìm kiếm danh sách nhà trọ / căn hộ cho thuê theo tiêu chí.

    Args:
        location (str): Khu vực / địa điểm muốn tìm (Ví dụ: 'Quận 1', 'Thủ Đức', 'Cầu Giấy')
        min_price (Optional[float]): Giá thuê tối thiểu (VNĐ/tháng)
        max_price (Optional[float]): Giá thuê tối đa (VNĐ/tháng)
        property_type (Optional[str]): Loại hình (Ví dụ: 'nhà trọ', 'căn hộ', 'chung cư', 'studio')
        bedrooms (Optional[int]): Số phòng ngủ (Ví dụ: 1, 2, 3)

    Returns:
        str: Danh sách các bất động sản phù hợp kèm thông tin cơ bản (giá, địa chỉ, loại hình)
    """
    # Mock data — mô phỏng dữ liệu trả về
    return (
        f"Kết quả tìm kiếm nhà trọ/căn hộ tại '{location}':\n"
        f"1. CH01 - Chung cư mini 45m² - Quận 1 - 5,000,000 VNĐ/tháng (2PN)\n"
        f"2. NT02 - Nhà trọ 25m² - Thủ Đức - 2,500,000 VNĐ/tháng (1PN)\n"
        f"3. CH03 - Căn hộ studio 35m² - Quận 3 - 4,000,000 VNĐ/tháng\n"
        f"4. NT04 - Phòng trọ 20m² - Cầu Giấy - 2,000,000 VNĐ/tháng\n"
        f"5. CH05 - Căn hộ 70m² - Quận 7 - 8,000,000 VNĐ/tháng (2PN)\n"
        f"(Dữ liệu mẫu — vui lòng lọc thêm nếu cần)"
    )


# =============================================================================
# 2. get_property_details — Xem chi tiết một bất động sản
# =============================================================================
def get_property_details(property_id: str) -> str:
    """
    Xem thông tin chi tiết của một bất động sản cụ thể.

    Args:
        property_id (str): Mã định danh của bất động sản (Ví dụ: 'CH01', 'NT02')

    Returns:
        str: Thông tin chi tiết bao gồm địa chỉ, giá, diện tích, mô tả, tiện ích, v.v.
    """
    # Mock data — mô phỏng dữ liệu trả về
    mock_properties = {
        "CH01": {
            "name": "Chung cư mini Quận 1",
            "address": "123 Nguyễn Huệ, Quận 1, TP.HCM",
            "price": "5,000,000 VNĐ/tháng",
            "area": "45m²",
            "bedrooms": 2,
            "type": "Chung cư mini",
            "description": "Căn hộ đầy đủ nội thất, gần trung tâm, an ninh tốt.",
            "amenities": ["WiFi", "Máy lạnh", "Tủ lạnh", "Máy giặt", "Thang máy"],
        },
        "NT02": {
            "name": "Nhà trọ Thủ Đức",
            "address": "456 Lê Văn Việt, Thủ Đức, TP.HCM",
            "price": "2,500,000 VNĐ/tháng",
            "area": "25m²",
            "bedrooms": 1,
            "type": "Nhà trọ",
            "description": "Phòng trọ sạch sẽ, có gác lửng, gần trường ĐH.",
            "amenities": ["WiFi", "Máy lạnh", "Nhà bếp riêng"],
        },
    }
    prop = mock_properties.get(property_id.upper())
    if prop:
        return (
            f"📋 Chi tiết bất động sản [{property_id.upper()}]:\n"
            f"  Tên: {prop['name']}\n"
            f"  Địa chỉ: {prop['address']}\n"
            f"  Giá: {prop['price']}\n"
            f"  Diện tích: {prop['area']}\n"
            f"  Phòng ngủ: {prop['bedrooms']}\n"
            f"  Loại hình: {prop['type']}\n"
            f"  Mô tả: {prop['description']}\n"
            f"  Tiện ích: {', '.join(prop['amenities'])}"
        )
    return f"LỖI: Không tìm thấy bất động sản với mã '{property_id}'."


# =============================================================================
# 3. check_viewing_availability — Kiểm tra lịch trống xem nhà
# =============================================================================
def check_viewing_availability(property_id: str, date: str) -> str:
    """
    Kiểm tra khung giờ trống để đặt lịch xem nhà cho một bất động sản.

    Args:
        property_id (str): Mã định danh bất động sản (Ví dụ: 'CH01')
        date (str): Ngày muốn xem (Định dạng: 'DD-MM-YYYY', Ví dụ: '01-08-2026')

    Returns:
        str: Danh sách các khung giờ còn trống trong ngày
    """
    # Mock data — mô phỏng dữ liệu trả về
    return (
        f"Kiểm tra lịch xem nhà [{property_id.upper()}] vào ngày {date}:\n"
        f"  ✅ 08:00 - 09:00 (Còn trống)\n"
        f"  ❌ 09:00 - 10:00 (Đã đặt)\n"
        f"  ✅ 10:00 - 11:00 (Còn trống)\n"
        f"  ✅ 14:00 - 15:00 (Còn trống)\n"
        f"  ❌ 15:00 - 16:00 (Đã đặt)\n"
        f"  ✅ 16:00 - 17:00 (Còn trống)\n"
        f"(Dữ liệu mẫu — vui lòng chọn giờ phù hợp)"
    )


# =============================================================================
# 4. book_viewing — Đặt lịch xem nhà
# =============================================================================
def book_viewing(
    property_id: str,
    date: str,
    time: str,
    name: str,
    phone: str,
    email: Optional[str] = None,
    note: Optional[str] = None,
) -> str:
    """
    Đặt lịch hẹn xem nhà / căn hộ trực tiếp.

    Args:
        property_id (str): Mã định danh bất động sản muốn xem (Ví dụ: 'CH01')
        date (str): Ngày muốn xem (Định dạng: 'DD-MM-YYYY', Ví dụ: '01-08-2026')
        time (str): Khung giờ muốn xem (Ví dụ: '08:00', '10:00', '14:00')
        name (str): Họ tên người đặt lịch
        phone (str): Số điện thoại liên hệ
        email (Optional[str]): Địa chỉ email (tùy chọn, để nhận xác nhận)
        note (Optional[str]): Ghi chú thêm (tùy chọn, Ví dụ: 'Muốn xem cùng bạn bè')

    Returns:
        str: Thông báo xác nhận đặt lịch thành công hoặc thất bại
    """
    # Mock data — giả lập đặt lịch thành công
    viewing_id = f"VIEW-{property_id.upper()}-{date.replace('-', '')}-{time.replace(':', '')}"
    return (
        f"✅ ĐẶT LỊCH XEM NHÀ THÀNH CÔNG!\n"
        f"  Mã lịch hẹn: {viewing_id}\n"
        f"  Bất động sản: {property_id.upper()}\n"
        f"  Thời gian: {date} lúc {time}\n"
        f"  Người đặt: {name}\n"
        f"  Điện thoại: {phone}\n"
        f"{'  Email: ' + email if email else ''}\n"
        f"{'  Ghi chú: ' + note if note else ''}\n"
        f"📌 Vui lòng đến đúng giờ. Liên hệ hotline 1900xxxx nếu cần hỗ trợ."
    )


# =============================================================================
# 5. cancel_viewing — Hủy lịch xem nhà
# =============================================================================
def cancel_viewing(viewing_id: str) -> str:
    """
    Hủy một lịch hẹn xem nhà đã đặt trước đó.

    Args:
        viewing_id (str): Mã lịch hẹn cần hủy (Ví dụ: 'VIEW-CH01-20260801-0800')

    Returns:
        str: Thông báo kết quả hủy lịch
    """
    # Mock data — giả lập hủy thành công
    return (
        f"✅ HỦY LỊCH XEM NHÀ THÀNH CÔNG!\n"
        f"  Mã lịch hẹn đã hủy: {viewing_id}\n"
        f"📌 Mọi thắc mắc vui lòng liên hệ hotline 1900xxxx."
    )


# =============================================================================
# 6. get_my_viewings — Xem danh sách lịch hẹn của tôi
# =============================================================================
def get_my_viewings(phone: str) -> str:
    """
    Xem tất cả các lịch hẹn xem nhà đã đặt theo số điện thoại.

    Args:
        phone (str): Số điện thoại đã dùng để đặt lịch (Ví dụ: '0901234567')

    Returns:
        str: Danh sách các lịch hẹn xem nhà (đã đặt, sắp tới, đã hủy)
    """
    # Mock data — giả lập danh sách lịch hẹn
    return (
        f"📋 DANH SÁCH LỊCH HẸN CỦA SỐ ĐIỆN THOẠI {phone}:\n"
        f"  1. VIEW-CH01-01082026-1000 — CH01 (Chung cư mini Q.1) — 01/08/2026 10:00 — ✅ Đã xác nhận\n"
        f"  2. VIEW-NT02-03082026-1400 — NT02 (Nhà trọ Thủ Đức) — 03/08/2026 14:00 — ⏳ Chờ xác nhận\n"
        f"  3. VIEW-CH05-28072026-0800 — CH05 (Căn hộ Q.7) — 28/07/2026 08:00 — ❌ Đã hủy\n"
        f"(Dữ liệu mẫu — 3 lịch hẹn gần đây nhất)"
    )


# =============================================================================
# DANH SÁCH TOOL ĐĂNG KÝ CHO REACT AGENT
# =============================================================================
AVAILABLE_TOOLS = {
    "search_properties": search_properties,
    "get_property_details": get_property_details,
    "check_viewing_availability": check_viewing_availability,
    "book_viewing": book_viewing,
    "cancel_viewing": cancel_viewing,
    "get_my_viewings": get_my_viewings,
}