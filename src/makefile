PKGDIR = /usr/share/pyhearts

all: 
	@../tools/py-compile *.py 

clean:
	rm -fv *.pyc *.pyo *~ *.bak *.gladep *.o *.so

install:
	mkdir -p $(DESTDIR)/usr/share/pyhearts
	mkdir -p $(DESTDIR)/usr/share/pyhearts/data
	mkdir -p $(DESTDIR)/usr/share/pyhearts/data/img
	install -m755 *.pyc $(DESTDIR)/$(PKGDIR)/.
	install -m755 *.py $(DESTDIR)/$(PKGDIR)/.
	install -m644 data/img/. $(DESTDIR)/$(PKGDIR)/data/img/.

