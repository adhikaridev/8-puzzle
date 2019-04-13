import resource
a = 1.646323154
a = round(a,2)
print a
print str(round((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024)),8))