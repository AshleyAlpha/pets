from django.test import TestCase
from django.test import TestCase
from .models import Project,Profile, Votes

class ProjectTestClass(TestCase):
       def setUp(self):
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali',first_name='hello',last_name='okay',phone_number=908787)
          self.project=Project(id=1,screenshot='@heroo',name='koko',description="koko koko koko okruuuuuu",overall_grade=2,url='halooooooo')
          self.grade=Grade(id=1,design=2,usability=2,content=2,project=self.project,total=0,avg=3,comment='olright')


       def tearDown(self):
           Profile.objects.all().delete()
           Project.objects.all().delete()
           Grade.objects.all().delete()

       def test_save_project(self):
         self.project.save_project()
         projects = Project.objects.all()
         self.assertTrue(len(projects) > 0)   

       def test_delete_project(self):
           self.project.save_project()
           self.project.delete_project()
           projects = Project.objects.all()
           self.assertTrue(len(projects) == 0) 

       def test_update_description(self):
           self.project.save_project()
           caption='kiki'
           self.project.update_description(caption)
           self.assertTrue( self.project.description == caption) 

class ProfileTestClass(TestCase):
       def setUp(self):
          
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali',first_name='hello',last_name='okay',phone_number=908787)
          self.project=Project(id=1,screenshot='@heroo',name='koko',description="koko koko koko okruuuuuu",overall_grade=2,url='halooooooo')
          self.grade=Grade(id=1,design=2,usability=2,content=2,project=self.project,total=0,avg=3,comment='olright')
        
       def tearDown(self):
          Profile.objects.all().delete()
          Project.objects.all().delete()
          Grade.objects.all().delete()
       
       def test_save_profile(self):
         self.profile.save_profile()
         profiles = Profile.objects.all()
         self.assertTrue(len(profiles) > 0) 

        
       def test_delete_profile(self):
           self.profile.save_profile()
           self.profile.delete_profile()
           profiles = Profile.objects.all()
           self.assertTrue(len(profiles) == 0)  


class VotesTestClass(TestCase):
       def setUp(self):
          
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali',first_name='hello',last_name='okay',phone_number=908787)
          self.project=Project(id=1,screenshot='@heroo',name='koko',description="koko koko koko okruuuuuu",overall_grade=2,url='halooooooo')
          self.grade=Grade(id=1,design=2,usability=2,content=2,project=self.project,total=0,avg=3,comment='olright')

       def tearDown(self):
          Profile.objects.all().delete()
          Project.objects.all().delete()
          Grade.objects.all().delete()
        
  
       def test_save_vote(self):
         self.profile.save_profile()
         self.project.save_project()
         self.grade.save_grade()
         grades = Grade.objects.all()
         self.assertTrue(len(grades) > 0) 

        
       def test_delete_vote(self):
           self.profile.save_profile()
           self.project.save_project()
           self.grade.save_grade()
           self.grade.delete_grade()
           grades = Grade.objects.all()
           self.assertTrue(len(grades) == 0)  

       
