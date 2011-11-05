# revision 23369
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-simplefonts
# catalog-date 2011-06-19 22:13:53 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-simplefonts
Version:	20110619
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
Conflicts:	texlive-texmf <= 20110705-3

%description
The package defines a set of commands for dealing with a new
font in ConTeXt.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/simplefonts/t-simplefonts.lua
%{_texmfdistdir}/tex/context/third/simplefonts/t-simplefonts.tex
%doc %{_texmfdistdir}/doc/context/third/simplefonts/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
