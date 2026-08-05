# class siunhan:
#     stt = 1
#     so_thu_tu = 1
#     suc_manh = 50

#     def __init__(self,para_ten,para_vu_khi,para_mau_sac):
#         self.ten = "sieunhan" + para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#         self.stt = siunhan.so_thu_tu
#         siunhan.so_thu_tu += 1


# sieu_nhan_A = siunhan("Sieu nhan do", "kiem", "do")
# sieu_nhan_B = siunhan("sieu nhan vang", "bua", "vang")


    # def xin_chao(self):

    #     return "xin chao,ta chinh la" + self.ten
    



# sieu_nhan_A = siunhan("kteam","knowledge", "tim")

# _

# siunhan.suc_manh = 40


# print(siunhan.suc_manh)
# print(sieu_nhan_A.suc_manh)

# print(sieu_nhan_A.xin_chao())
# print(siunhan.xin_chao(sieu_nhan_A))
   

# sieu_nhan_A = siunhan()

# sieu_nhan_A.ten = "sieu_nhan_do"
# sieu_nhan_A.vu_khi = "kiem"
# sieu_nhan_A.mau_sac = "Do"


# class sieunhan:
#     suc_manh =50
#     def __init__(self,para_ten,para_vu_khi,para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mausac = para_mau_sac 

#     @classmethod
#     def from_string(cls, s):
#         lst = s.split("-")
#         new_lst = [st.strip() for st in lst]
#         ten, vu_khi, mau_sac = new_lst
#         return cls(ten, vu_khi, mau_sac)
# infor_str = "do - kiem -Do"
# sieu_nhan_A = sieunhan.from_string(infor_str)
# print(sieu_nhan_A.__dict__)




#lopwkethua

# class Sieunhan:
#     suc_manh = 50
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac):
#         self.ten = para_ten
#         self.vukhi = para_vu_khi
#         self.mausac = para_mau_sac 
#     def __str__(self):
#         return "Day laf{}, su dung {}".format(self.ten, self.mausac)

# class SieunhanKteam(Sieunhan):
#     suc_manh = 40
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_linh_vat):
#         # self.ten = para_ten 
#         # self.vukhi = para_vu_khi
#         # self.mausac = para_mau_sac 
#         super.__init__(para_ten, para_vu_khi, para_mau_sac )
#         self.linhvat = para_linh_vat

# SN_A = Sieunhan("sieunhando","kiem","do") 
# SN_B = Sieunhan("sieunhanxanh","kiem","xanh")
# print(SN_A)
# Kteam_do = SieunhanKteam("do", "cung", "do", "Lai_anh_anh")

# print(Kteam_do.suc_manh)
# print(Kteam_do.__dict__)


class Kter:
    def __init__ (self, ho, ten):
        self.ho = ho
        self.ten = ten
        # self.email = ho + "-" + ten + "@kteam.com"
    @property
    def ho_va_ten(self):
        return "{}{}".format(self.ho, self.ten)
    
    @property
    def emails(self):
        return self.ho + " _" + self.ten + "@kteam.com"

    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(" ")
        self.ho = ho_moi
        self.ten = ten_moi

    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print("da xoa")

kter_A = Kter("Tran", "Long dep trai")
kter_A.ho_va_ten = " Nguyen_Giau"

# kter_A.ho = "Nguyen"
# kter_A.ten = "Anh"

# print(kter_A.ho)
# print(kter_A.ten)
# print(kter_A.emails)
print(kter_A.ho_va_ten)
del kter_A.ho_va_ten
print(kter_A.ho_va_ten)






                            