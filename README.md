# Projet_BTC
Dépôt de code de Capo-chichi Inès et Hiruthayaraj Marianne, pré-ing2 BTC 1

Le graphique en ligne "Fecal live bacteria" est réussi mais il est mal cadré à l'ouverture donc on ne voit pas correctement la légende. Les 2 autres graphiques ont un problème d'échelle qui fait que l'on n'obtient pas les bons graphiques. Nous pensons qu'il y a une erreur dans l'extraction des données en colonne ou dans l'échelle prises pour l'axe des ordonnées et/ou des abscisses.

La fonction "axes.grid(6)" fournit 2 graphiques au lieu d'un seul (on a un premier graphique avec aucunes données mais des carreaux et un second avec les données mais sans carreaux). On l'a donc remplacé par "plt.grid(6)" qui fournit un graphique avec les données et les carreaux dans le fond. Egalement pour les graphiques, les titres des graphiques et des axes disparraissent avec "axes", nous l'avons donc remplacé par "plt". Globalement lorsque nous utilisons "axes" au lieu de "plt", des errreurs apparaissent.
