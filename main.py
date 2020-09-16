import doctest

import control


def main():
    """
    Übergibt dem Controller die TermeApp Klasse.
    :rtype: object
    """
    controller = control.TermeApp()

    """Start ist im StartScreen / Hauptmenue."""
    controller.run()


if __name__ == '__main__':
    """Wird eingesetzt, um die Python Datei als eigenständiges Programm zu nutzen und 
    einzelne Elemente dieser Datei importierbar zu machen. 
    Der Mechanismus wird auch dazu genutzt, komplexe Modultests du implementieren."""
    # doctest.testmod()

    main()
