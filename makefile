SUBDIRS = src
PYFILES = $(wildcard *.py)
PKGNAME = pyhearts
VERSION = 0.1
PYTHON = python
SRCDIR = src
MISCDIR=misc
PIXDIR = pixmaps

subdirs:
	for d in $(SUBDIRS); do make -C $$d; [ $$? = 0 ] || exit 1 ; done

clean:
	for d in $(SUBDIRS); do make -C $$d clean ; done

install:
	mkdir -p $(DESTDIR)/usr/share/pyhearts
	mkdir -p $(DESTDIR)/usr/share/pixmaps/pyhearts
	mkdir -p $(DESTDIR)/usr/share/applications
	mkdir -p $(DESTDIR)/usr/bin
	install -m644 COPYING $(DESTDIR)/usr/share/pyhearts/.
	install -m644 $(PIXDIR)/*.png $(DESTDIR)/usr/share/pixmaps/pyhearts/.
	install -m755 $(MISCDIR)/pyhearts $(DESTDIR)/usr/bin/.
	chmod +x $(DESTDIR)/usr/bin/pyhearts
	install -m644 $(MISCDIR)/pyhearts.desktop $(DESTDIR)/usr/share/applications/.
	for d in $(SUBDIRS); do make DESTDIR=$(DESTDIR) -C $$d install; [ $$? = 0 ] || exit 1; done
