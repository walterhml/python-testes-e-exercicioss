medida = float(input('uma distacia em metros: '))
cm = medida * 100
mm = medida * 1000
quilometro = medida * 100000
micrometro = medida * 10000
milimetro = medida * 10
polegada = medida * 2.54

print(
    'A medida {}m corresponde \n a {}cm \n {}mm \n quilometro {}km \n micrometro: {} \n milimetro {} \n polegada {} '.format(
        medida, cm, mm, quilometro, micrometro, milimetro, polegada))
