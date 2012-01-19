# revision 25094
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-simplefonts
# catalog-date 2011-12-28 10:22:06 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-simplefonts
Version:	20111228
Release:	1
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
%{_texmfdistdir}/tex/context/third/simplefonts/t-simplefonts.tex
%doc %{_texmfdistdir}/doc/context/third/simplefonts/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
