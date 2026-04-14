from bigtree import Node

abuelo = Node("Carlos (abuelo)")
papa   = Node("Miguel (padre)", parent=abuelo)
tia    = Node("Lucía (tía)",    parent=abuelo)
Node("Diego",  parent=papa)
Node("Sofía",  parent=papa)
Node("Andrés", parent=tia)

abuelo.show()