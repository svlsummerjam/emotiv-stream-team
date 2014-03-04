SUBDIRS = streamteam

bin_SCRIPTS = emotiv-stream-team
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = emotiv-stream-team.in

do_substitution = sed -e "s,[@]pythondir[@],$(pythondir),g"\ 
	-e "s,[@]PACKAGE[@],$(PACKAGE),g" \ 
	-e "s,[@]VERSION[@],$(VERSION),g" 

emotiv-stream-team: emotiv-stream-team.in Makefile
	$(do_substitution) < $(srcdir)/emotiv-stream-team.in > emotiv-stream-team
	chmod +x emotiv-stream-team