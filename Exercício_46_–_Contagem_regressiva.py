{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Exercício 46 – Contagem regressiva",
      "provenance": [],
      "mount_file_id": "1bPp2vBiXpRs7KA6_UTnu-_OP7UFE8FO5",
      "authorship_tag": "ABX9TyPnxMtHkT/TV9vVG8AioW+u",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/samucale/Curso_em_Video/blob/main/Exerc%C3%ADcio_46_%E2%80%93_Contagem_regressiva.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0-eOcmytWxbr"
      },
      "source": [
        "# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XEtQpCqiWDVX",
        "outputId": "9e75e9c7-ae60-4f0b-a14c-bc8b5a9f1c1e"
      },
      "source": [
        "#from time import sleep#\n",
        "for cont in range (10,-1,-1):\n",
        "    print(cont)\n",
        "    sleep(0.5)\n",
        "print ('BUM....BUM...BRUM')    "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "0\n",
            "BUM....BUM...BRUM\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WYTG3rQXY1RM",
        "outputId": "ebbd04eb-7a52-4157-df7f-d5b27af052be"
      },
      "source": [
        "for cont in range (0,11):\n",
        "  print (cont)\n",
        "  sleep (1.0)\n",
        "print ('COOORRAAAAA')  "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n",
            "COOORRAAAAA\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PBUqECclZLaN"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}