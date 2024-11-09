def ontcijfer(bericht, sleutel):
    ontcijferd_bericht = ""
    for teken in bericht:
        if teken  in sleutel:
            ontcijferd_bericht += teken

    return ontcijferd_bericht