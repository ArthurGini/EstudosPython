# Codigo baseado em:
# https://medium.com/@shivama205/audio-signals-comparison-23e431ed2207


#correlation.py
#import subprocess ERRO AQUIIII
import subprocess
import numpy

# seconds to sample audio file for
#Segundos do sample audio file
sample_time = 500

# number of points to scan cross correlation over
#Numero de pontos para scanear a correlação entre os arquivos
span = 150

# step size (in points) of cross correlation
step = 1
# minimum number of points that must overlap in cross correlation
# exception is raised if this cannot be met
min_overlap = 20
# report match when cross correlation has a peak exceeding threshold
threshold = 0.5

#Calculando a impressao digital da musica(fingerprint)
def calculate_fingerprint(filename):
    fpcalc_out = subprocess.getoutput('fpcalc -raw -length %i %s' % (sample_time, filename))
    fingerprint_index = fpcalc_out.find('FINGERPRINT=') + 12

    #Convertendo a impressao digital para uma lista de inteiros
    fingerprints = map(int, fpcalc_out[fingerprint_index:].split(','))

    return fingerprints

#Retorna a correlação das listas
def correlation(listX, listY):
    if len(listX) == 0 or len(listY) == 0:
        # Error checking in main program should prevent us from ever being
        # able to get here.

        raise Exception("Listas vazias nao podem ser calculadas")
    if len(listX) > len(listY):
        listX = listX[:len(listY)]
        #se o X > Y o listX é a listaX a partir do ultimo da listaY
    elif len(listY) > len(listX):
        listY = listY[:listX]

    covariance = 0
    for i in range(len(listX)):
        covariance += 32 - bin(listX[i] ^ listY[i]).count("1")
    covariance = covariance/float(len(listX))

    return covariance/32

#Retorna a correlação cruzada coma listY compensa listX
def cross_correlation(listX, listY, offset):
    if offset > 0:
        listX = listX[offset:]
        listY = listY[:len(listX)]
    elif offset <0:
        offset = -offset
        listY = listY[offset:]
        listX = listX[:len(listY)]
    if min(len(listX), len(listY)) < min_overlap:
        # Error checking in main program should prevent us from ever being
        # able to get here.
        return
    return correlation(listX, listY)

# cross correlate listx and listy with offsets from -span to span
# Correlação cruzada de listX e listY com offsets entre -span e span
def compare(listX, listY, span, step):
    if span > min(len(listX), len(listY)):
        """# Error checking in main program should prevent us from ever being
        # able to get here."""
        raise Exception('span >= sample size: %i >= %i \n' % (span, min(len(listX), len(listY))) + 'Reduce span, reduce crop or increase sample_time.')
        
    corr_XY = []

    for offset in numpy.arange(-span, span +1, step):
        corr_XY.append(cross_correlation(listX, listY, offset))
    return corr_XY

#Retorna o valor maximo do indice na lista
def max_index(listX):
    max_index = 0
    max_value = listX[0]

    for i, value in enumerate(listX):
        if value > max_value:
            max_value = value
            max_index = i
    return max_index

def get_max_corr(corr, source, target):
    max_corr_index = max_index(corr)
    max_corr_offset = -span + max_corr_index * step
    print("max_corr_index = ", max_corr_index, "max_corr_offset= ", max_corr_offset)

    #mostrando matches
    if corr[max_corr_index] > threshold:
        print('%s and %s match with correlation of %.4f at offset %i'
            % (source, target, corr[max_corr_index], max_corr_offset))
        

def correlate(source, target):
    fingerprint_source = calculate_fingerprint(source)
    fingerprint_target = calculate_fingerprint(target)

    corr = compare(fingerprint_source, fingerprint_target, span, step)
    max_corr_offset = get_max_corr(corr, source, target)

    return