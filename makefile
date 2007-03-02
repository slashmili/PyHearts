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
	mkdir -p $(DESTDIR)/usr/share
	mkdir -p $(DESTDIR)/usr/share/games	
	mkdir -p $(DESTDIR)/usr/share/games/pyhearts
	mkdir -p $(DESTDIR)/usr/share/games/pyhearts/bin
	mkdir -p $(DESTDIR)/usr/share/games/pyhearts/data
	mkdir -p $(DESTDIR)/usr/share/games/pyhearts/data/img	

	mkdir -p $(DESTDIR)/usr/games/
	
		
	mkdir -p $(DESTDIR)/usr/share/pixmaps/pyhearts
	mkdir -p $(DESTDIR)/usr/share/applications

	install -m644 COPYING $(DESTDIR)/usr/share/games/pyhearts/.
	install -m644 $(PIXDIR)/*.png $(DESTDIR)/usr/share/pixmaps/pyhearts/.

	install -m755 $(MISCDIR)/pyhearts $(DESTDIR)/usr/games/.
	chmod +x $(DESTDIR)/usr/games/pyhearts
	
	install -m644 $(MISCDIR)/pyhearts.desktop $(DESTDIR)/usr/share/applications/.

	
	install -m644 img/*.gif $(DESTDIR)/usr/share/games/pyhearts/data/img/.
	install -m644 img/*.png $(DESTDIR)/usr/share/games/pyhearts/data/img/.
	install -m644 img/copying $(DESTDIR)/usr/share/games/pyhearts/data/img/.
	for d in $(SUBDIRS); do make DESTDIR=$(DESTDIR) -C $$d install; [ $$? = 0 ] || exit 1; done
