def EstaEntre(HoraReferida, Horas):
    if HoraReferida >= min(Horas) and HoraReferida <= max(Horas):
        return True;
    else:
        return False;