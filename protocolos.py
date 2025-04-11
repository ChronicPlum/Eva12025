OSPF = 110
RIP =120
EIGRP = 90
BGP = 20


x = input("Distancia administrativa?(OSPF, RIP, EIGRP, BGP): ")

if x == ("OSPF"):
    print("La distancia administrativa de OSPF es : " + str(OSPF))
elif x == ("RIP"):
    print("La distancia administrativa de RIP es : "+ str(RIP))
elif x == ("EIGRP"):
    print("La distancia administrativa de EIGRP es : " + str(EIGRP))
elif x == ("BGP"):
    print("La distancia administrativa de BGP es : " + str(BGP))

else:
    print("Ingrese uno de los protocolos mencionados anteriormente (OSPF, RIP, EIGRP, BGP)")
