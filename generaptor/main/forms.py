from django import forms


class DrawForm(forms.Form):
    file = open("main/files/draws.txt", 'r', encoding="utf-8")
    draws = file.readlines()
    file.close()


class EatForm(forms.Form):
    file = open("main/files/eats.txt", 'r', encoding="utf-8")
    eats = file.readlines()
    file.close()


class ListenForm(forms.Form):
    file = open("main/files/listens.txt", 'r', encoding="utf-8")
    listens = file.readlines()
    file.close()


class PlayForm(forms.Form):
    file = open("main/files/plays.txt", 'r', encoding="utf-8")
    plays = file.readlines()
    file.close()


class WatchForm(forms.Form):
    file = open("main/files/watches.txt", 'r', encoding="utf-8")
    watches = file.readlines()
    file.close()


class DoingForm(forms.Form):
    file = open("main/files/doings.txt", 'r', encoding="utf-8")
    doings = file.readlines()
    file.close()