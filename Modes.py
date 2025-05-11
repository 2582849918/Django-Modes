from django.db import models


class Feature(models.Model):
    """功能信息表"""
    name = models.CharField(max_length=100, unique=True, verbose_name="功能名称", help_text="功能名称")
    version = models.CharField(max_length=50, verbose_name="版本", help_text="版本")
    release_date = models.DateTimeField(verbose_name="发布日期", help_text="功能的发布日期")
    force_upgrade = models.BooleanField(default=False, verbose_name="强制升级", help_text="是否需要强制升级")
    related_models = models.ManyToManyField('Model', related_name='features', verbose_name="关联模型", blank=True, )
    shared_libraries = models.ManyToManyField('SharedLibrary', related_name='features', verbose_name="共享库",
                                              blank=True, help_text="关联的共享库")
    unpacking_records = models.ManyToManyField('UnpackingRecord', related_name='features', verbose_name="解包记录",
                                               blank=True, help_text="关联的解包记录")
    executable = models.ManyToManyField('Executable', related_name='features', verbose_name="可执行文件", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    class Meta:
        verbose_name = "功能"
        verbose_name_plural = "功能"
        ordering = ['-release_date']
        db_table = 'version_feature'

    def __str__(self):
        return f"{self.name} - {self.version}"


class Model(models.Model):
    """模型信息表"""
    name = models.CharField(max_length=100, unique=True, verbose_name="模型名称", help_text="模型名称")
    type = models.CharField(max_length=20, default="models", verbose_name="类型", help_text="模型类型")
    version = models.CharField(max_length=50, verbose_name="版本", help_text="版本")
    release_date = models.DateTimeField(verbose_name="发布日期", help_text="模型的发布日期")
    interface_modified = models.BooleanField(default=False, verbose_name="接口变更", help_text="接口是否发生变化")
    folder = models.CharField(max_length=255, verbose_name="下载路径", help_text="文件下载路径（空表示根目录）",
                              blank=True, default='')
    force_upgrade = models.BooleanField(default=False, verbose_name="强制升级", help_text="是否需要强制升级")
    cn_addr = models.JSONField(verbose_name="国内下载地址", help_text="文件的国内下载地址")
    foreign_addr = models.JSONField(verbose_name="国外下载地址", help_text="文件的国外下载地址")
    oss_addr = models.JSONField(verbose_name="OSS下载地址", help_text="文件的OSS下载地址")
    size = models.PositiveIntegerField(default=0, verbose_name="模型大小", help_text="模型文件的大小（单位：字节）")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    class Meta:
        verbose_name = "模型"
        verbose_name_plural = "模型"
        ordering = ['-release_date']
        db_table = 'version_model'

    def __str__(self):
        return f"{self.name} - {self.version}"


class Executable(models.Model):
    """可执行文件信息表"""
    name = models.CharField(max_length=100, unique=True, verbose_name="可执行文件名称", help_text="可执行文件名称")
    type = models.CharField(max_length=20, default="exe", verbose_name="类型", help_text="可执行文件")
    version = models.CharField(max_length=50, verbose_name="版本", help_text="版本")
    release_date = models.DateTimeField(verbose_name="发布日期", help_text="可执行文件的发布日期")
    folder = models.CharField(max_length=255, verbose_name="下载路径", help_text="文件下载路径（空表示根目录）",
                              blank=True, default='')
    force_upgrade = models.BooleanField(default=False, verbose_name="强制升级", help_text="是否需要强制升级")
    oss_addr = models.JSONField(verbose_name="OSS下载地址", help_text="文件的OSS下载地址")
    size = models.PositiveIntegerField(default=0, verbose_name="可执行文件大小",
                                       help_text="可执行文件的大小（单位：字节）")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    class Meta:
        verbose_name = "可执行文件"
        verbose_name_plural = "可执行文件"
        ordering = ['-release_date']
        db_table = 'version_executable'

    def __str__(self):
        return f"{self.name} - {self.version}"


class SharedLibrary(models.Model):
    """共享库信息表"""
    name = models.CharField(max_length=100, unique=True, verbose_name="共享库名称", help_text="共享库名称")
    type = models.CharField(max_length=20, default="sharelib", verbose_name="类型", help_text="共享库")
    version = models.CharField(max_length=50, verbose_name="版本", help_text="版本")
    release_date = models.DateTimeField(verbose_name="发布日期", help_text="共享库的发布日期")
    folder = models.CharField(max_length=255, verbose_name="下载路径", help_text="文件下载路径（空表示根目录）",
                              blank=True, default='')
    force_upgrade = models.BooleanField(default=False, verbose_name="强制升级", help_text="是否需要强制升级")
    oss_addr = models.JSONField(verbose_name="OSS下载地址", help_text="文件的OSS下载地址")
    size = models.PositiveIntegerField(default=0, verbose_name="共享库大小", help_text="共享库的大小（单位：字节）")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    class Meta:
        verbose_name = "共享库"
        verbose_name_plural = "共享库"
        ordering = ['-release_date']
        db_table = 'version_shared_library'

    def __str__(self):
        return f"{self.name} - {self.version}"


class UnpackingRecord(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, unique=True, verbose_name="解压名称")
    from_type = models.CharField(max_length=20, blank=True)
    from_name = models.CharField(max_length=50, blank=True)
    source_path = models.CharField(max_length=255, verbose_name="源路径")
    target_file_name = models.CharField(max_length=255, verbose_name="目标文件名称", blank=True)
    target_dir = models.CharField(max_length=255, verbose_name="目标路径", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'version_unpacking_record'
        verbose_name = "解压信息"
        verbose_name_plural = "解压信息"

    def __str__(self):
        return f"UnpackingRecord({self.source_path} -> {self.target_file_name})"
