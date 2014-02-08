# revision 27171
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-simplefonts
# catalog-date 2012-07-26 08:34:30 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-simplefonts
Version:	20120726
Release:	2
Summary:	Simplified font usage for ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-simplefonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simplefonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simplefonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The package defines a set of commands for loading and using
fonts in ConTeXt.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/simplefonts/t-simplefonts.lua
%{_texmfdistdir}/tex/context/third/simplefonts/t-simplefonts.mkii
%{_texmfdistdir}/tex/context/third/simplefonts/t-simplefonts.mkiv
%doc %{_texmfdistdir}/doc/context/third/simplefonts/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120726-1
+ Revision: 812177
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111228-1
+ Revision: 762596
- Update to latest upstream package

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110619-3
+ Revision: 750519
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110619-2
+ Revision: 745200
- texlive-context-simplefonts

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110619-1
+ Revision: 718142
- texlive-context-simplefonts
- texlive-context-simplefonts
- texlive-context-simplefonts
- texlive-context-simplefonts

