# revision 29229
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-simplefonts
# catalog-date 2012-08-13 18:29:21 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-simplefonts
Version:	20120813
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
