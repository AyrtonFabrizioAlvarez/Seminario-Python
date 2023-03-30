evalue = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures.
"""

separated = evalue.split("resumen:")
title = separated[0]
body = separated[1]


wordsTitle = title.replace(" título:", "").split().__len__()
print(f"el titulo tiene {wordsTitle} palabras")

easy = 0
aceptable = 0
hard = 0
veryHard = 0

for sentence in body.split("."):
    wordsSentence = sentence.split().__len__()
    print(f"La oracion tiene {wordsSentence} palabras")
    if 0 < wordsSentence < 13:
        easy += 1
    elif wordsSentence < 18:
        aceptable += 1
    elif wordsSentence < 26:
        hard += 1
    else:
        veryHard+= 1

print(f"faciles: {easy}")
print(f"aceptables: {aceptable}")
print(f"dificiles: {hard}")
print(f"muy dificiles: {veryHard}")



