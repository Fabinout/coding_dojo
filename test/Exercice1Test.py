from src.DeadCell import DeadCell
from src.LivingCell import LivingCell

__author__ = 'fabienlamarque'

import unittest


class Exercice1Test(unittest.TestCase):

    def test_testFramework(self):
        self.assertEquals(0, 0)

    def test_une_cellule_vivante_avec_moins_de_deux_voisins_meurt(self):
        cell = LivingCell().withNeighbors(LivingCell())
        nextCell = cell.nextStep()
        self.assertTrue(nextCell.isDead())

    def test_une_cellule_vivante_avec_exactement_deux_voisins_survit(self):
        cell = LivingCell().withNeighbors(LivingCell(), LivingCell())
        nextCell = cell.nextStep()
        self.assertTrue(nextCell.isAlive())

    def test_une_cellule_vivante_vavec_une_cellule_vivante_et_une_morte_meurt(self):
        cell = LivingCell().withNeighbors(LivingCell(), DeadCell())
        nextCell = cell.nextStep()
        self.assertTrue(nextCell.isDead())

    def test_une_cellule_vivante_avec_trois_cellule_vivante_survit(self):
        cell = LivingCell().withNeighbors(LivingCell(), LivingCell(), LivingCell())
        nextCell = cell.nextStep()
        self.assertTrue(nextCell.isAlive())

    def test_une_cellule_morte_avec_deux_voisins_vivants_reste_morte(self):
        cell = DeadCell().withNeighbors(LivingCell(), LivingCell())
        nextCell = cell.nextStep()
        self.assertTrue(nextCell.isDead)

    def test_cellule_morte_renait_si_3_voisins_vivants(self):
        cell = DeadCell().withNeighbors(LivingCell(), LivingCell(), LivingCell())
        nextCell = cell.nextStep()
        self.assertTrue(nextCell.isAlive())


if __name__ == '__main__':
    unittest.main()
