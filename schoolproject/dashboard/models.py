from django.db import models

# Create your models here.
class CompFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comp_first_year'


class CompFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comp_fourth_year'


class CompSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comp_second_year'


class CompThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comp_third_year'


class BeedFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'beed_first_year'



class BeedSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'beed_second_year'



class BeedThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'beed_third_year'


class BeedFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'beed_fourth_year'


class BtledFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'btled_first_year'


class BtledSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'btled_second_year'


class BtledThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'btled_third_year'


class BtledFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'btled_fourth_year'


class CivilFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'civil_first_year'


class CivilSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'civil_second_year'


class CivilThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'civil_third_year'


class CivilFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'civil_fourth_year'


class ElectFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'elect_first_year'


class ElectSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'elect_second_year'


class ElectThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'elect_third_year'


class ElectFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'elect_fourth_year'


class MechaFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mecha_first_year'


class MechaSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mecha_second_year'


class MechaThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mecha_third_year'


class MechaFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mecha_fourth_year'


class AutoFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'auto_first_year'


class AutoSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'auto_second_year'


class AutoThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'auto_third_year'


class AutoFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'auto_fourth_year'


class ComgentFirstYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comgent_first_year'


class ComgentSecondYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comgent_second_year'


class ComgentThirdYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comgent_third_year'


class ComgentFourthYear(models.Model):
    course_id = models.AutoField(primary_key=True)
    instructor_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField()
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=120)
    department = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'comgent_Fourth_year'






