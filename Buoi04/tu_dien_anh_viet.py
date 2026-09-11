# Hoạt động 5: Vận dụng - Từ điển Anh - Việt
tu_dien_anh_viet = {
    "hello": "xin chào", 
    "book": "quyển sách", 
    "table": "cái bàn" 
} 
# Tra tu 
print(tu_dien_anh_viet.get("hello", "Không tìm thấy từ này")) 
print(tu_dien_anh_viet.get("computer", "Không tìm thấy từ này")) 
# Them tu moi 
tu_dien_anh_viet["computer"] = "máy tính" 
# Xoa mot tu 
tu_dien_anh_viet.pop("table") 
print("Từ điển hiện tại:") 
for tu_anh, tu_viet in tu_dien_anh_viet.items(): 
 print(f"{tu_anh} - {tu_viet}")
