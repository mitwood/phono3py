intel_root = "/projects/sems/install/rhel7-x86_64/sems/compiler/intel/16.0.1/base"
mkl_root = "%s/mkl" % intel_root
compiler_root = "/projects/sems/install/rhel7-x86_64/sems/compiler/gcc/6.1.0/base/" 

mkl_extra_link_args_lapacke = ['-L%s/lib/intel64' % mkl_root,
                               '-lmkl_rt']
mkl_extra_link_args_lapacke += ['-L%s/lib/intel64' % compiler_root,
#                                '-lsvml',
                                '-liomp5',
#                                '-limf',
                                '-lpthread']
mkl_include_dirs_lapacke = ["%s/include" % mkl_root]
