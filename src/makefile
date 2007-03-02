PKGDIR = /usr/share/games/pyhearts/bin

all: 
	@../tools/py-compile *.py 

clean:
	rm -fv *.pyc *.pyo *~ *.bak *.gladep *.o *.so

install:
	mkdir -p $(DESTDIR)/usr/share/games/pyhearts/bin

		
	install -m755 *.pyc $(DESTDIR)/$(PKGDIR)/.
	install -m755 *.py $(DESTDIR)/$(PKGDIR)/.

		

