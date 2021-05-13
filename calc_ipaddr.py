#!/usr/bin/env python
# -*- coding: utf-8 _*_

# 表示形式	10進数表示 2進数表示 16進数表示
# IPアドレス	192.168.0.1
# サブネットマスク	/24 (255.255.255.0)
# ネットワークアドレス
# (開始IP)	192.168.0.0
# ホストアドレス
# (使用可能IP)	192.168.0.1
# ～
# 192.168.0.254
# ブロードキャストアドレス
# (終了IP)	192.168.0.255
# アドレス数	IPアドレス数：256 （ホストアドレス数：254）
# IPアドレスクラス	クラスC

class IpAddress:

    @classmethod
    def cidr_to_nomal(cidr):
        return cidr_normal[cidr]

    def __init__(self, ipaddr, netmask):
        self.ipaddr                 = ipaddr                            # '192.168.100.1'のような文字列
        self.ipaddrbin            = IpAddress.ipaddr_to_ipaddrbin(ipaddr)
        self.netmask             = netmask              # 255.255.255.0のような文字列
        self.netmaskbin        = IpAddress.ipaddr_to_ipaddrbin(netmask)
        self.networkaddrbin = IpAddress.get_network_ipaddrbin(self.ipaddrbin, self.netmaskbin)
        self.networkaddr      = IpAddress.binipaddr_to_ipaddr(self.networkaddrbin)

    # 10進数表記のIPアドレス（例：192.168.100.1'）を数値に変換する
    @staticmethod
    def ipaddr_to_ipaddrbin(ipaddr):
        BYTE_LEN =8
        ipaddrs = ipaddr.split('.')

        b = 0b0
        for octet_str in ipaddrs:
            b = (b << BYTE_LEN) | int(octet_str)
            
        return b

    #  数値のIPアドレスを10進数表記のIPアドレス（例：192.168.100.1'）へ変換する
    @staticmethod
    def binipaddr_to_ipaddr(ipaddrbin):
        BYTE_LEN =8
        MASK = 0b11111111

        b = ipaddrbin
        ip = ""
        octets = []
        for i in range(4):
            octet = b & MASK
            octets.append(str(octet))
            b >>= BYTE_LEN

        octets.reverse()
        return ".".join(octets)


    #  数値のIPアドレスを10進数表記のIPアドレス（例：192.168.100.1'）へ変換する
    @staticmethod
    def get_network_ipaddrbin(ipaddrbin, netmaskbin):
        print(netmaskbin)
        return ipaddrbin & netmaskbin
    
    @staticmethod
    def slash_notation_to_netmaskbin(num):
        binstr = ('1' * num) + ('0' * (32 - num))
        return int(binstr, 2)

    def __str__(self):
        pass
    
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 1:
        print("no args err")
        exit
    
    split = sys.argv[1].split("/")
    print(split)
    netmaskbin = IpAddress.slash_notation_to_netmaskbin(int(split[1]))
    netmaskstr = IpAddress.binipaddr_to_ipaddr(netmaskbin)
    
    ipobj = IpAddress(split[0], netmaskstr)
    print(ipobj.networkaddr)
    
    
